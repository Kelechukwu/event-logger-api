
# future functions needed for BUSINESS LOGIC can be put here

def parse_query_string(query):
    GREATER_THAN_OR_EQUAL = ' gte '
    EQUALS = ' eq '
    OR = ' OR '
    AND = ' AND '
    CONTAINS = ' ct '

    query = query.replace('(', 'Q(')
    query = query.replace('Q(Q(', 'Q(').replace('))', ')')
    query = query.replace(GREATER_THAN_OR_EQUAL, '__gte=')
    query = query.replace(EQUALS, '__exact=')
    query = query.replace(CONTAINS, '__icontains=')
    query = query.replace(AND, ' & ').replace(OR, ' | ')

    return query
