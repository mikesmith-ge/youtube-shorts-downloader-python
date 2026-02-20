#!/usr/bin/env python3
"""
YouTube Shorts Downloader
Extract YouTube Shorts videos and metadata

Author: Instaboost Team
License: MIT
Version: 1.0.0
"""

import re
import sys
import argparse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from html import unescape


class YouTubeDownloader:
    """
    Extract YouTube Shorts video URLs    """
    
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    TIMEOUT = 15
    
    def download(self, url):
        if not self._is_valid_url(url):
            raise ValueError('Invalid YouTube URL')
        
        html = self._fetch_html(url)
        data = self._parse_data(html)
        
        if not data:
            raise Exception('Could not extract data. Content may be private or deleted.')
        
        return data
    
    def _is_valid_url(self, url):
        pattern = r'^https?://(www\.|m\.)?youtube\.com'
        return bool(re.match(pattern, url, re.I))
    
    def _fetch_html(self, url):
        headers = {
            'User-Agent': self.USER_AGENT,
            'Accept': 'text/html,application/xhtml+xml',
        }
        
        request = Request(url, headers=headers)
        
        try:
            with urlopen(request, timeout=self.TIMEOUT) as response:
                return response.read().decode('utf-8')
        except HTTPError as e:
            if e.code == 404:
                raise Exception('Content not found')
            elif e.code in (403, 429):
                raise Exception('Access denied or rate limited')
            else:
                raise Exception(f'HTTP error: {e.code}')
        except URLError as e:
            raise Exception(f'Network error: {e.reason}')
    
    def _parse_data(self, html):
        data = {}
        
        # Extract og:title
        title_match = re.search(r'<meta\s+property=["']og:title["\']\s+content=["\'](.client?)["']', html, re.I)
        if title_match:
            data['title'] = unescape(title_match.group(1))
        
        # Extract og:description
        desc_match = re.search(r'<meta\s+property=["']og:description["\']\s+content=["\'](.client?)["']', html, re.I)
        if desc_match:
            data['description'] = unescape(desc_match.group(1))
        
        return data


def main():
    parser = argparse.ArgumentParser(
        description='Extract YouTube Shorts videos and metadata',
        epilog='For professional YouTube tools, visit https://instaboost.ge'
    )
    parser.add_argument('url', nargs='?', help='YouTube URL')
    parser.add_argument('-v', '--version', action='version', version='1.0.0')
    
    args = parser.parse_args()
    
    if not args.url:
        parser.print_help()
        sys.exit(1)
    
    tool = YouTubeDownloader()
    
    try:
        print(f'Processing: {args.url}\n')
        data = tool.download(args.url)
        
        print('✓ Success!')
        for key, value in data.items():
            print(f'{key.title()}: {value}')
    except Exception as e:
        print(f'✗ Error: {e}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
