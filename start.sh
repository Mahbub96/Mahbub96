#!/bin/bash

organize_and_archive() {
    local source_folder="$1"
    # local archive_folder="/home/dmin/Archive"  # Change this to the folder where you want to archive files
	local archive_folder="$HOME/Archive" # Change this to the folder where you want to archive files


    # Create the hierarchical folders based on file dates
    for file in "$source_folder"/*; do
        if [ -f "$file" ]; then
            # Extract the modification date of the file
            file_date=$(date -r "$file" '+%d-%b-%y')
            month=$(date -r "$file" '+%b-%y')

            # Create the month folder if it doesn't exist
            month_folder="${source_folder}/${month}"
            mkdir -p "$month_folder"

            # Create the date subfolder if it doesn't exist
            date_folder="${month_folder}/${file_date}"
            mkdir -p "$date_folder"

            # Move the file to the date subfolder
            mv "$file" "${date_folder}/"
        fi
    done

    # Archive files that haven't been modified for more than one month
    find "$source_folder" -type f -mtime +30 -exec mv {} "$archive_folder" \;
}

get_hadith() {
    local url="https://random-hadith-generator.vercel.app/bukhari/"
    local json_response=$(curl -s "$url")
    
    if ! command -v jq &> /dev/null; then
        echo "jq is not installed. Please install it before running this script."
        exit 1
    fi
    
    hadith_english=$(echo "$json_response" | jq -r '.data.hadith_english')
    refno=$(echo "$json_response" | jq -r '.data.refno')
}

display_hadith() {
    local bold=$(tput bold)
    local reset=$(tput sgr0)
    local color_green=$(tput setaf 2)
    local color_red=$(tput setaf 1)
    
    echo -e "${bold}${color_green}+------------ الرَّحِيْمِ الرَّحْمٰنِ اللهِ بِسْمِ ------------+${reset}"
    echo -e "${bold}${color_green}|${reset} ${color_red}$hadith_english${reset}${bold}${color_green} ${reset}"
    echo -e "${bold}${color_green}+------------------------------------------------+${reset}"
    echo "${bold}$refno${reset}"
}




