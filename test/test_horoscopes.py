# #!/usr/bin/env python
#
# import re
#
# from src import templater
# from src import config_handler as cfgh
# from src.modules import horoscopes as hs
#
# '''
# TODO: Mock responses, do not actually get the horoscopes for each test.
#       It takes a lot of time and unnecessary processing power, look at tests
#       for quotes.
# '''
#
#
# def test_website_names_included_in_template():
#     hs_config = _get_hs_config()
#     html_email = _get_built_email()
#
#     website_names = map(lambda hs: hs.get('website_name'), hs_config)
#
#     for name in website_names:
#         assert name in html_email
#
#
# def test_website_urls_included_in_template():
#     hs_config = _get_hs_config()
#     html_email = _get_built_email()
#
#     website_urls = map(lambda hs: hs.get('website_url'), hs_config)
#
#     for url in website_urls:
#         assert url in html_email
#
#
# def test_horoscope_line_formatting():
#     html_email = _get_built_email()
#
#     # This expression matches one formatted horoscope line
#     # with arbitrary content for url and name
#     hs_line_exp = '<h3><a href="(http(s?)://.+)">(.+)</a></h3><p>(.+)</p>'
#
#     match = re.search(hs_line_exp, html_email)
#
#     assert match is not None
#
#
# def test_divider_count():
#     hs_config = _get_hs_config()
#     html_email = _get_built_email()
#
#     hr_element_count = [m.start() for m in re.finditer('<hr/>', html_email)]
#
#     # Every horoscope should have a divider below it except for the last one
#     assert len(hr_element_count) == (len(hs_config) - 1)
#
#
# def _get_built_email():
#     hs_config = _get_hs_config()
#     horoscopes = hs.get(hs_config)
#     html_email = templater.build(horoscopes, None)
#     return html_email
#
#
# def _get_hs_config():
#     return cfgh.default_config().get('horoscopes')
