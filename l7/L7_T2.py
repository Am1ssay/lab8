def find_mx_bfstr(search_query):
    search_query = search_query.lower()
    mx_bfstr = ""
    mx = 0

    for i in range(len(search_query)):
        for j in range(i + 1, len(search_query) + 1):
            substr = search_query[i:j]
            count = search_query.count(substr)

            if count > mx or (count == mx and len(substr) > len(mx_bfstr)):
                mx_bfstr = substr
                mx = count

    return mx_bfstr, mx


def get_user_input():
    user_input = input()
    return user_input


if __name__ == "__main__":
    search_query = get_user_input()
    print(find_mx_bfstr(search_query))
