import requests
import csv

# Define the base URLs for the APIs
api_base_urls = ['https://api.raritysniper.com/public/collection/volted-dragons-sailors-club/id/', 'https://api.raritysniper.com/public/collection/command-z/id/', 'https://api.raritysniper.com/public/collection/waterbomb-league/id/', 'https://api.raritysniper.com/public/collection/the-warriors-of-ankh/id/', 'https://api.raritysniper.com/public/collection/alienanimatedpunkz/id/', 'https://api.raritysniper.com/public/collection/deltanauts-alpha-gold/id/', 'https://api.raritysniper.com/public/collection/deltanauts-alpha-silver/id/', 'https://api.raritysniper.com/public/collection/deltanauts-alpha-bronze/id/', 'https://api.raritysniper.com/public/collection/wilder-moto-genesis/id/', 'https://api.raritysniper.com/public/collection/tribe-odyssey/id/', 'https://api.raritysniper.com/public/collection/wgmis/id/', 'https://api.raritysniper.com/public/collection/balloon-town/id/', 'https://api.raritysniper.com/public/collection/moon-lizzys/id/',
                 'https://api.raritysniper.com/public/collection/rare-apepe-yc/id/', 'https://api.raritysniper.com/public/collection/surfn-learn-to-earn/id/']
# Create an empty list to store the NFT data
nft_data = []

# Loop through the base URLs
for api_base_url in api_base_urls:
    nft_id = 1
    while True:
        url = f'{api_base_url}{nft_id}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            nft_id = data['nftId']
            rarity_score = data['rarityScore']
            rank = data['rank']
            nft_data.append([str(api_base_url), str(nft_id), rarity_score, rank])  # Convert nft_id to string
            nft_id += 1
        else:
            print(f'Request failed with status code {response.status_code} for URL {url}')
            break

# Write the data to separate CSV files for each API base URL
start = 111
for i, api_base_url in enumerate(api_base_urls):
    with open(f'nft_data{start+i}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['API', 'NFT ID', 'Rarity Score', 'Rank'])
        for row in nft_data:
            if row[0].startswith(api_base_url):  # Only write rows for the current API
                writer.writerow(row)
