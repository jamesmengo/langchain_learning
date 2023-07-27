import os
import requests


def scrape_linkedin_profile(linkedin_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from a LinkedIn profile given the URL."""

    # api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    # api_key = os.environ.get("PROXYCURL_API_KEY")
    # header_dic = {'Authorization': 'Bearer ' + api_key}
    # params = {
    #     'url': 'https://www.linkedin.com/in/james-meng/',
    #     'fallback_to_cache': 'on-error',
    #     'use_cache': 'if-present',
    #     'skills': 'include',
    #     'inferred_salary': 'include',
    #     'personal_email': 'include',
    #     'personal_contact_number': 'include',
    #     'twitter_profile_id': 'include',
    #     'facebook_profile_id': 'include',
    #     'github_profile_id': 'include',
    #     'extra': 'include',
    # }
    # response = requests.get(api_endpoint,
    #                         params=params,
    #                         headers=header_dic)

    gist_response = requests.get(
        "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
    )
    # read the gist_response
    data = gist_response.json()
    # remove any values with empty fields, None, or empty string values
    # remove any keys for  certifications and people_also_viewed
    data = {
        k: v
        for k, v in data.items()
        if v not in (None, "", []) and k not in ["certifications", "people_also_viewed"]
    }

    return data
