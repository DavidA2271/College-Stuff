import BikeIndexRESTAPI


class Demo:
    ''' Runs the program with default search parameters '''
    def __init__(self) -> None:
        self.params = None
    def run(self):
        if self.params is None:
            self.params = BikeIndexRESTAPI.Search_Params()
        br = BikeIndexRESTAPI.Bike_Response(self.params)
        br.query()
        br.get_images()
        br.save_data()


if __name__ == '__main__':
    demo = Demo()
    demo.run()
