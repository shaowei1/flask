class Myflask():

    def route(self, rule, **options):
        def decorator(f):
            endpoint = options.pop('endpoint', None)
            # self.add_url_rule(rule, endpoint, f, **options)
            return f

        return decorator


if __name__ == '__main__':
    app = Myflask()


    @app.route('/', methods=['POST', 'POST'], endpoint='?')
    def index():
        return 'xxx'


    print(index())
