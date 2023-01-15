
exec(open("Modified_data/realtime.py").read())
exec(open("Modified_data/rocket.dr").read())

trick.trick_view_add_auto_load_file("TV_rocket.tv")
trick.stop(100)