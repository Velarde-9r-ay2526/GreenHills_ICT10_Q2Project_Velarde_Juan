from pyscript import display

# Dictionary containing Southeast Asian countries and their nicknames
sea_nicknames = {
    'brunei': 'The Abode of Peace',
    'cambodia': 'The Land of the Khmers',
    'east timor': 'The Land of the Rising Sun of Southeast Asia',
    'indonesia': 'The Emerald of the Equator',
    'laos': 'The Land of a Million Elephants',
    'malaysia': 'Truly Asia',
    'myanmar': 'The Land of the Golden Pagodas',
    'philippines': 'The Pearl of the Orient Seas',
    'singapore': 'The Lion City',
    'thailand': 'The Land of Smiles',
    'vietnam': 'The Land of the Ascending Dragon'
}

# Converting keys into a list to check available countries if needed
available_countries = list(sea_nicknames.keys())

def get_country_nickname(event):
    # Getting input element from HTML
    from js import document
    
    input_box = document.getElementById("country_input")
    raw_input = input_box.value
    
    # Cleaning the string input using lower() and strip()
    clean_country = raw_input.strip().lower()
    
    # Check if input is empty
    if clean_country == "":
        message = "<p class='text-amber-700 text-sm font-medium'>Please enter a country name.</p>"
    # Checking if user input exists in our dictionary
    elif clean_country in sea_nicknames:
        nickname = sea_nicknames[clean_country]
        message = f"<p class='text-emeraldDeep font-serif font-bold text-lg'>Nickname: <span class='font-normal italic'>{nickname}</span></p>"
    else:
        message = "<p class='text-rose-700 text-sm font-medium'>Country not found in Southeast Asia. Try another one!</p>"
        
    # Display the result inside #output_box
    output_div = document.getElementById("output_box")
    output_div.innerHTML = message