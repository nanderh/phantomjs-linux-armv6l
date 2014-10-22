## progress.py

It's sometimes hard to figure where you are in the build process.
If you use nohup to output the progress of the build progress you can use this python script to check the progress.
Edit the script so it takes either the stable or the development reference output file.
It takes the standard <code>build.sh.out</code> file and compares it to the reference.
It does not clean the input so it might give a false indication if the line appears twice in the reference.

So edit the script and run it with <code>python /reference.py</code>