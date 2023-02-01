# Benign traffic generator
The script will use a file with urls as input. The script visits each second one of those websites, while accepting the cookies. By accepting the cookies also the advertisements and other links on the website will get loaded. You could run this script while running a packet capture to generate a packet capture with benign traffic.

## Requirements
Linux system with the following packages:
`python3`
`lynx`

## Setup
`pip install -r requirements.txt`

## Example
For example you could use the alexa top x list to generate valid data. 
`wget -q http://s3.amazonaws.com/alexa-static/top-1m.csv.zip;unzip top-1m.csv.zip; awk -F ',' '{print $2}' top-1m.csv|head -10000 > top-10000.txt; rm top-1m.csv*`
make urls from the domains
`sed 's/^/https:\/\//' top-10000.txt > top-1000https.txt`

And run the script:
`./generator.py -f top-1000https.txt`

 ## Parameters
 `-f, --file | input pcapfile`

 ## Authors

- Robert Cranendonk https://github.com/RACranendonk
- Tom Grolleman https://github.com/tgrolleman