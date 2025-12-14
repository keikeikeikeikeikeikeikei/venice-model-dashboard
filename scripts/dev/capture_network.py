#!/usr/bin/env python3
"""
Capture network requests from Venice video models page using Playwright.
This script will open the page, scroll to trigger dynamic content, and log all network requests.
"""
import asyncio
import json
import pathlib
from playwright.async_api import async_playwright

async def capture_network_requests():
    network_log = []
    quote_requests = []
    
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        # Set up network request listener
        def handle_request(request):
            network_log.append({
                'url': request.url,
                'method': request.method,
                'resource_type': request.resource_type,
            })
            print(f"[{request.method}] {request.url}")
        
        # Set up response listener to capture quote API responses
        async def handle_response(response):
            if '/video/quote' in response.url:
                try:
                    # Get request body
                    request_body = None
                    if response.request.method == 'POST':
                        try:
                            request_body = response.request.post_data
                        except:
                            pass
                    
                    # Get response body
                    response_body = await response.json()
                    
                    quote_requests.append({
                        'url': response.url,
                        'status': response.status,
                        'request_body': request_body,
                        'response': response_body
                    })
                    print(f"  💰 Quote response: {response_body}")
                except Exception as e:
                    print(f"  ⚠️  Could not parse response: {e}")
        
        page.on('request', handle_request)
        page.on('response', handle_response)
        
        # Navigate to the page
        print("Navigating to https://docs.venice.ai/models/video...")
        await page.goto('https://docs.venice.ai/models/video', wait_until='networkidle')
        
        # Wait a bit for initial load
        await asyncio.sleep(2)
        
        # Scroll down to trigger lazy loading
        print("\nScrolling down to trigger dynamic content...")
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        
        # Wait for any additional requests
        await asyncio.sleep(5)
        
        # Ensure data directory exists
        data_dir = pathlib.Path(__file__).parent.parent / 'data'
        data_dir.mkdir(exist_ok=True)
        
        # Save the network log
        output_file = data_dir / 'network_log.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(network_log, f, indent=2)
        
        # Save quote requests separately
        quote_file = data_dir / 'video_quote_requests.json'
        with open(quote_file, 'w', encoding='utf-8') as f:
            json.dump(quote_requests, f, indent=2)
        
        print(f"\n✅ Captured {len(network_log)} network requests")
        print(f"📄 Saved to {output_file}")
        print(f"\n💰 Captured {len(quote_requests)} video quote API calls")
        print(f"📄 Saved to {quote_file}")
        
        # Show sample quote data
        if quote_requests:
            print(f"\n🔍 Sample quote data:")
            for req in quote_requests[:3]:
                print(f"  Request: {req.get('request_body', 'N/A')[:100]}...")
                print(f"  Response: {req['response']}")
        
        await browser.close()
    
    return network_log, quote_requests

if __name__ == '__main__':
    asyncio.run(capture_network_requests())

