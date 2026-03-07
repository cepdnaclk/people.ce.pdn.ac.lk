GLOBAL_IDX_SETTINGS = {
    "minWordSizefor1Typo": 4,
    "minWordSizefor2Typos": 8,
    "hitsPerPage": 10,
    "maxValuesPerFacet": 100,
    "numericAttributesToIndex": None,
    "attributesToRetrieve": None,
    "unretrievableAttributes": None,
    "optionalWords": None,
    "attributesToHighlight": None,
    "paginationLimitedTo": 100,
    "exactOnSingleWordQuery": "attribute",
    "ranking": [
        "typo",
        "geo",
        "words",
        "filters",
        "proximity",
        "attribute",
        "exact",
        "custom",
    ],
    "separatorsToIndex": "",
    "removeWordsIfNoResults": "none",
    "queryType": "prefixLast",
    "highlightPreTag": "<em>",
    "highlightPostTag": "</em>",
    "alternativesAsExact": ["ignorePlurals", "singleWordSynonym"],
}

STUDENTS_IDX_SETTINGS = {
    **GLOBAL_IDX_SETTINGS,
    "searchableAttributes": [
        "title",
        "reg_no",
        "name_formats.preferred_short_name",
        "unordered(name_formats.full_name)",
        "unordered(name_formats.preferred_long_name)",
        "unordered(name_formats.name_with_initials)",
        "unordered(current_affiliation)",
        # "unordered(content)",
        "unordered(metadata.emails.personal)",
        "unordered(metadata.emails.university)",
        "unordered(location)",
        "unordered(interests)",
    ],
    "attributesForFaceting": [
        "searchable(interests)",
        "batch",
        "searchable(current_affiliation)",
        "role",
    ],
    "attributesToSnippet": ["snippet:20", "content:10"],
    "attributeForDistinct": "chunk",
    "disableTypoToleranceOnAttributes": [
        "location",
        "metadata.emails.personal",
        "metadata.emails.university",
        "name_formats.full_name",
        "name_formats.preferred_short_name",
    ],
    "customRanking": ["desc(batch)"],
    "renderingContent": {
        "facetOrdering": {
            "facets": {"order": ["batch", "current_affiliation"]},
            "values": {
                "batch": {"sortRemainingBy": "count"},
                "current_affiliation": {"sortRemainingBy": "count"},
            },
        }
    },
}

STAFF_IDX_SETTINGS = {
    **GLOBAL_IDX_SETTINGS,
    "searchableAttributes": [
        "title",
        "unordered(name_formats.full_name)",
        "unordered(current_affiliation)",
        "unordered(interests)",
        # "unordered(content)",
        "unordered(metadata.emails.university)",
        "unordered(department)",
    ],
    "attributesForFaceting": [
        "searchable(interests)",
        "searchable(current_affiliation)",
        "searchable(department)",
        "role",
    ],
    "attributesToSnippet": ["content:10"],
    "disableTypoToleranceOnAttributes": [
        "metadata.emails.university",
        "name_formats.full_name",
    ],
    "customRanking": ["asc(role)", "asc(title)"],
    "renderingContent": {
        "facetOrdering": {
            "facets": {"order": ["current_affiliation", "department", "role"]},
            "values": {
                "current_affiliation": {"sortRemainingBy": "count"},
                "department": {"sortRemainingBy": "count"},
                "role": {"sortRemainingBy": "alpha"},
            },
        }
    },
}
