import subprocess
import os

# Get get list of directories in current directory
dir_names = filter(os.path.isdir, os.listdir(os.getcwd()))

for dirname in dir_names:

    os.chdir(dirname)
    fnames = [fname for fname in subprocess.check_output(['ls', '-lA1']).split('\n') if 'mp4' in fname]

    # Generate intermediate files for concate later
    script = 'ffmpeg -i "{0}" -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate{1}.ts'

    # Generate shell script to do actual encoding, makes it easier to
    # debug if something goes wrong
    final_script = open('encode.sh', 'w')

    for i, f in enumerate(fnames):
        print script.format(f, i)
        final_script.write('{0}\n'.format(script.format(f, i)))
        i += 1

    combined = ''
    for i in xrange(0, len(fnames)):
        combined += 'intermediate{0}.ts|'.format(i)

    combined = combined[:-1]

    # Concat all intermediate files and remove intermediate files
    merge_cmd = 'ffmpeg -i "concat:{0}" -c copy -bsf:a aac_adtstoasc output.mp4'

    final_script.write('{0}\n'.format(merge_cmd.format(combined, dirname)))
    final_script.write('rm *.ts\n')
    final_script.close()

    # Run shell script and cleanup once encoding is done
    subprocess.call(['sh', 'encode.sh'])
    subprocess.call(['rm', 'encode.sh'])
    subprocess.call(['mv', 'output.mp4', '../{0}.mp4'.format(dirname)])

    os.chdir('..')

