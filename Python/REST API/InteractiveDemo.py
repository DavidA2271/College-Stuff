from Demo import Demo
import BikeIndexRESTAPI


class InteractiveDemo(Demo):
    ''' Inherits from Demo. Has increased functionality for bike search parameters. '''
    def __init__(self, params) -> None:
        self.set_params(params)
    def set_params(self, params):
        per_page = params['per_page']
        location = params['location']
        distance = params['distance']
        self.params = BikeIndexRESTAPI.Search_Params(per_page=per_page, location=location, distance=distance)


class InputHandler:
    ''' Handles input received from console window '''
    def get_params(self):
        ''' Asks the user for input '''
        self.params = {}
        print('Hit enter after answering each question. You may leave blank answers for default results.')
        inp = input('How many bikes do you want to request? (Max 100, Default 10):    ')
        self.params['per_page'] = inp if inp != '' else '10'
        inp = input('What location? (Default New York, NY):    ')
        self.params['location'] = inp if inp != '' else 'New York, NY'
        inp = input('How many miles from the location? (Default 10):    ')
        self.params['distance'] = inp if inp != '' else '10'
    def check_input(self):
        ''' Makes sure given input is the correct data type '''
        per_page = self.params['per_page']
        distance = self.params['distance']
        if per_page is not None:
            if not per_page.isdigit():
                return False
        if distance is not None:
            if not distance.isdigit():
                return False
        return True



if __name__ == '__main__':
    ih = InputHandler()
    ih.get_params()
    if ih.check_input():
        id = InteractiveDemo(ih.params)
        id.run()
    else:
        print('Some parameters were not of the correct type.')
        print('Request amount must be integer, location can be address, city and state, or zip code, and distance must be an integer.')