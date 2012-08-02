django-compass-watches
======================

This simple script that allows you to watch multiple compass directories inside a django project at the same time.

Installation
----
1. Place the `compass_watch.py` script in the root directory of your django project
2. `$ chmod +x compass_watch.py` to be able to execute it
3. Insert the `COMPASS_DIR` tuple inside the `settings.py` of your django project specifying the folders that you want to watch:
<pre>
    # - This is just an example -
    COMPASS_DIRS = (
        os.path.join(PROJECT_ROOT, 'apps/whatever/static/any/compass/project'),
        STATIC_ROOT + 'path/to/any/compass/project',
    )
</pre>
Ensure yourself to have a config.rb file inside every folder that you want to watch

Usage
----
Just run the script from your django project root with
<pre>
$ ./compass_watch.py
</pre>
and you will be able to modify every `.sass` or `.scss` inside your compass projects with real-time compiling in css.

This allows you to have different target directories or configurations between multiple applications that use compass 