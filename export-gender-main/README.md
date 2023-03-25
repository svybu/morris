### API usage
APi is running from API_start.py.

    http://127.0.0.1:3000/?name=Carlos
This request will give a response like:

    {"name": "Carlos", "gender": "male"}

### Console usage for .csv files

    python get_gender_from_csv.py <path_to_original_file> <path_to_result_file>


### Console usage generate_pie_chart.py for .csv files

    python generate_pie_chart.py <path_to_file.csv>

### Start in Docker
    
    docker build . -t gender_api

    docker run -d -p 3000:3000 gender_api

### Count_comments with terminal output

     python count_comments.py <path_to_file.csv>

### Count_comments with chart(top-50 + others)

    python count_comments.py <path_to_file.csv> -c




