def get_soup (file_name):
    f = open(file_name, 'r')
    response_text = f.read()
    f.close()
    soup = BeautifulSoup(response_text)
    return soup