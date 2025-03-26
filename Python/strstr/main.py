import kmp
import regex_practice


def main():
    print(kmp.kmp("abcabcabc", 'abc'))
    print(kmp.kmp("abcabcabc", 'bca'))
    print(kmp.kmp("abcabcabc", 'x'))
    print(kmp.kmp("abcabcabc", 'cba'))
    print(kmp.kmp("123%*^&*jnsadjbgiwebgviwefgv", 'w'))
    print(kmp.kmp("123%*^&*jnsadjbgiwebgviwefgv ", ' '))
    print(kmp.kmp("123%*^&*jnsadjbgiwebgviwefgv ", '^'))


    print(regex_practice.search_email())
    print(regex_practice.search_dates())
    print(regex_practice.search_phones())
    print(regex_practice.search_urls())
    print(regex_practice.search_color_codes())


if __name__ == '__main__':
    main()