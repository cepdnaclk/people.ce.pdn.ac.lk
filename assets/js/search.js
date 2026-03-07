(function ($, algoliasearch, bootstrap) {
  "use strict";

  var config = window.ALGOLIA_CONFIG || {};
  var placeholderRegex = /PLACEHOLDER/i;
  var hasValidConfig =
    config.appId &&
    config.searchApiKey &&
    !placeholderRegex.test(config.appId) &&
    !placeholderRegex.test(config.searchApiKey);

  var SELECTORS = {
    form: "[data-algolia-search-form]",
    input: "[data-algolia-search-input]",
    clear: "[data-algolia-search-clear]",
    help: "[data-algolia-search-help]",
  };

  function getForms() {
    return $(SELECTORS.form);
  }

  function getInputs() {
    return $(SELECTORS.input);
  }

  function getClearButtons() {
    return $(SELECTORS.clear);
  }

  function getHelpers() {
    return $(SELECTORS.help);
  }

  var $results = $("#algolia-search-results");
  var $status = $("#algolia-search-status");
  var $count = $("#algolia-search-count");
  var $loader = $("#algolia-search-loader");
  var $paginationWrapper = $("#algolia-search-pagination");
  var $paginationList = $paginationWrapper.find("ul");
  var modalElement = document.getElementById("algoliaSearchModal");
  var searchModal =
    modalElement && bootstrap && bootstrap.Modal ? new bootstrap.Modal(modalElement) : null;

  function trimText(value, maxLength) {
    return value.length > maxLength ? `${value.substring(0, maxLength)}...` : value;
  }

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  const TEXT_TRIM_LEN = 48;
  const HITS_PER_PAGE = 8;
  var allHits = [];
  var currentPage = 0;
  var currentQuery = "";
  var client =
    hasValidConfig && algoliasearch ? algoliasearch(config.appId, config.searchApiKey) : null;

  function disableSearch(reason) {
    var $helpers = getHelpers();
    if ($helpers.length) {
      $helpers.text(reason).removeClass("d-none");
    }
    getForms().addClass("disabled");
    getInputs().prop("disabled", true);
    getClearButtons().addClass("d-none");
  }

  function findClearButtonForInput($input) {
    return $input.closest("form").find(SELECTORS.clear).first();
  }

  function toggleClearButtonForInput($input) {
    var hasValue = Boolean(($input.val() || "").trim());
    var $clearButton = findClearButtonForInput($input);
    if ($clearButton.length) {
      $clearButton.toggleClass("d-none", !hasValue);
    }
  }

  function refreshClearButtons() {
    getInputs().each(function () {
      toggleClearButtonForInput($(this));
    });
  }

  function setQueryForAllInputs(query) {
    getInputs().val(query);
    refreshClearButtons();
  }

  function setLoading(isLoading) {
    if (isLoading) {
      $loader.removeClass("d-none");
      $results.empty();
      $paginationWrapper.addClass("d-none");
      $count.text("");
    } else {
      $loader.addClass("d-none");
    }
  }

  function updateStatus(message, isError) {
    if (!$status.length) {
      return;
    }
    $status.toggleClass("text-danger", Boolean(isError));
    $status.text(message);
  }

  function buildHitHtml(hit) {
    const url = hit.url || hit.relUrl || "#";
    var metadata = [];
    const affiliation = hit.current_affiliation;
    const location = hit.location;

    var highlight = hit._highlightResult || {};
    var highlightedFields = [
      highlight.name_formats && highlight.name_formats.preferred_long_name,
      highlight.name_formats && highlight.name_formats.full_name,
      highlight.title,
    ];
    var matchedField = highlightedFields.find(function (field) {
      return field && field.value && field.matchLevel == "full";
    });

    // Use highlighted matched field, preferred_long_name, or title
    const title =
      (matchedField && matchedField.value) ||
      (hit.name_formats && hit.name_formats.preferred_long_name) ||
      hit.title ||
      "-";

    // Use reg_no for the subtitle for students
    const subtitle = hit.reg_no ? `(${hit.reg_no})` : "";

    if (affiliation) {
      // Skip the default values to avoid noise in the results
      const affiliation_text = String(affiliation);
      if (
        !affiliation_text.includes("University of Peradeniya") &&
        !affiliation_text.includes("Department of Computer Engineering")
      )
        metadata.push({ text: trimText(affiliation_text, TEXT_TRIM_LEN), color: "bg-success" });
    }

    if (location) {
      metadata.push({ text: trimText(location, TEXT_TRIM_LEN), color: "bg-secondary" });
    }

    if (hit.role) {
      metadata.push({ text: hit.role, color: "bg-danger" });
    }

    const tagsString = metadata.length
      ? `<div class="mb-2 d-flex align-items-center flex-wrap gap-2">
        ${metadata.map((m) => `<span class="badge rounded-pill ${m.color}">${m.text}</span>`).join("")} </div>`
      : "";

    return `
      <a class="list-group-item list-group-item-action theme-bg-light" href="${escapeHtml(url)}">
      <h6 class="mb-1">${title} <small>${subtitle}</small></h6>
      ${tagsString}
      </a>
    `;
  }

  function renderPage(pageIndex) {
    currentPage = pageIndex;
    var start = pageIndex * HITS_PER_PAGE;
    var end = start + HITS_PER_PAGE;
    var pageHits = allHits.slice(start, end);
    $results.html(pageHits.map(buildHitHtml).join(""));

    var totalResults = allHits.length;
    if (totalResults === 0) {
      updateStatus("No results found");
      $paginationWrapper.addClass("d-none");
      $count.text("");
      return;
    }

    updateStatus(
      "Showing " + pageHits.length + " of " + totalResults + ' results for "' + currentQuery + '".'
    );
    $count.text("Page " + (pageIndex + 1) + " of " + Math.ceil(totalResults / HITS_PER_PAGE));

    renderPagination(totalResults, pageIndex);
  }

  function renderPagination(totalResults, pageIndex) {
    var totalPages = Math.ceil(totalResults / HITS_PER_PAGE);
    if (totalPages <= 1) {
      $paginationWrapper.addClass("d-none");
      $paginationList.empty();
      return;
    }

    var items = [];

    function addPageButton(label, page, disabled, active) {
      var classes = ["page-item"];
      if (disabled) {
        classes.push("disabled");
      }
      if (active) {
        classes.push("active");
      }
      items.push(`
        <li class="${classes.join(" ")}">
          <button class="page-link" type="button" data-page="${page}">${label}</button>
        </li>
      `);
    }

    function addEllipsis() {
      items.push('<li class="page-item disabled"><span class="page-link">...</span></li>');
    }

    addPageButton("Prev", Math.max(pageIndex - 1, 0), pageIndex === 0, false);

    var totalVisible = 5;
    var start = Math.max(pageIndex - 2, 0);
    var end = Math.min(start + totalVisible - 1, totalPages - 1);
    if (end - start + 1 < totalVisible) {
      start = Math.max(end - totalVisible + 1, 0);
    }

    if (start > 0) {
      addPageButton(1, 0, false, pageIndex === 0);
      if (start > 1) {
        addEllipsis();
      }
    }

    for (var i = start; i <= end; i += 1) {
      addPageButton(i + 1, i, false, i === pageIndex);
    }

    if (end < totalPages - 1) {
      if (end < totalPages - 2) {
        addEllipsis();
      }
      addPageButton(totalPages, totalPages - 1, false, pageIndex === totalPages - 1);
    }

    addPageButton(
      "Next",
      Math.min(pageIndex + 1, totalPages - 1),
      pageIndex === totalPages - 1,
      false
    );

    $paginationList.html(items.join(""));
    $paginationWrapper.removeClass("d-none");
  }

  function handlePaginationClick(event) {
    var target = $(event.target);
    var page = parseInt(target.data("page"), 10);
    if (Number.isNaN(page)) {
      return;
    }
    event.preventDefault();
    if (page === currentPage) {
      return;
    }
    renderPage(page);
  }

  // function sortHits(hits) {
  //   return hits.sort(function (a, b) {
  //     var scoreA = a._rankingInfo ? a._rankingInfo.userScore || 0 : 0;
  //     var scoreB = b._rankingInfo ? b._rankingInfo.userScore || 0 : 0;
  //     if (scoreA === scoreB) {
  //       var tyA = a.type || "";
  //       var tyB = b.type || "";
  //       return tyA.localeCompare(tyB);
  //     }
  //     return scoreB - scoreA;
  //   });
  // }

  function performSearch(query) {
    if (!hasValidConfig || !client) {
      return;
    }
    currentQuery = query;
    setQueryForAllInputs(query);
    setLoading(true);
    updateStatus('Searching for "' + query + '"...');
    if (searchModal) {
      searchModal.show();
    }

    var baseParams = {
      hitsPerPage: 100,
      highlightPreTag: "<mark>",
      highlightPostTag: "</mark>",
      getRankingInfo: true,
    };

    var queries = buildSearchQueries(query, baseParams);
    if (!queries.length) {
      setLoading(false);
      updateStatus("Search is not configured for this page.", true);
      return;
    }

    client
      .search(queries)
      .then(function (response) {
        var combined = [];
        if (response && response.results) {
          response.results.forEach(function (result) {
            var hits = Array.isArray(result.hits) ? result.hits : [];
            // Ensure unique hits by 'pageId'
            if (!combined._seenTargets) {
              combined._seenTargets = new Set();
            }

            hits.forEach(function (hit) {
              console.log(hit);
              var pageId = hit.url;
              if (pageId && combined._seenTargets.has(pageId)) {
                return; // Skip duplicate
              }

              if (pageId) {
                combined._seenTargets.add(pageId);
              }

              hit.__indexName = result.index;
              combined.push(hit);
            });
          });
        }

        // allHits = sortHits(combined);
        allHits = combined;

        setLoading(false);
        if (!allHits.length) {
          $results.empty();
          updateStatus('No results found for "' + query + '".');
          $count.text("");
          $paginationWrapper.addClass("d-none");
          return;
        }
        renderPage(0);
      })
      .catch(function (error) {
        setLoading(false);
        updateStatus("Search failed. Please try again later.", true);
        console.error("Algolia search error", error);
      });
  }

  if (!hasValidConfig) {
    disableSearch("Search is currently unavailable. Configure Algolia credentials to enable it.");
    return;
  }

  if (!getForms().length || !algoliasearch || !bootstrap) {
    return;
  }

  function buildSearchQueries(query, params) {
    var queries = [];
    queries.push({ indexName: "student_profiles", query: query, params: params });
    // queries.push({ indexName: "staff_profiles", query: query, params: params });

    return queries;
  }

  $(document).on("input", SELECTORS.input, function () {
    toggleClearButtonForInput($(this));
  });

  $(document).on("click", SELECTORS.clear, function (event) {
    event.preventDefault();
    var $button = $(this);
    var $form = $button.closest("form");
    var $input = $form.find(SELECTORS.input).first();
    $input.val("");
    toggleClearButtonForInput($input);
    $input.trigger("focus");
  });

  $(document).on("submit", SELECTORS.form, function (event) {
    event.preventDefault();
    var $form = $(this);
    var $input = $form.find(SELECTORS.input).first();
    var query = ($input.val() || "").trim();
    if (!query) {
      updateStatus("Enter a search term to begin.");
      return;
    }
    performSearch(query);
  });

  $paginationWrapper.on("click", "button.page-link", handlePaginationClick);

  if (modalElement) {
    modalElement.addEventListener("shown.bs.modal", function (event) {
      if (event.target === modalElement) {
        var $modalInput = $(modalElement).find(SELECTORS.input).first();
        if ($modalInput.length) {
          $modalInput.trigger("focus");
        } else {
          var $firstInput = getInputs().first();
          if ($firstInput.length) {
            $firstInput.trigger("focus");
          }
        }
      }
    });
  }

  refreshClearButtons();
})(window.jQuery, window.algoliasearch, window.bootstrap);
