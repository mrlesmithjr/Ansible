# 2018-10-14 (cc) <paul4hough@gmail.com>
#
# 2018-10-14 (cc) <paul4hough@gmail.com>
#
require 'shellwords'

$runstart = Time.now
testout_fn = "#{Dir.pwd}/rake-task.out"

at_exit {
  runtime = Time.now - $runstart
  sh "date '+%F-%X molecule test stop' >> #{testout_fn} "
  puts "run time: #{runtime}"
}

task :default => [:test,]
def bash cmd
    cmd = "set -o pipefail && #{cmd}"
    print(cmd)
    system("bash -c #{cmd.shellescape}")
    cmd_status = $?
    if cmd_status != 0
        raise "'#{cmd}' execution failed (exit code: #{cmd_status})"
    end
end

task :test,[:flags,:opts] do |task,args|
  sh "date '+%F-%X molecule test start' > #{testout_fn}"
  bash "molecule #{args[:flags]} test #{args[:opts]} 2>&1 | tee -a #{testout_fn}"
end
task :verify,[:flags,:opts] do |task,args|
  sh "date '+%F-%X molecule test start' > #{testout_fn}"
  bash "molecule #{args[:flags]} verify #{args[:opts]} 2>&1 | tee -a #{testout_fn}"
end
task :converge,[:flags,:opts] do |task,args|
  sh "date '+%F-%X molecule test start' > #{testout_fn}"
  bash "molecule #{args[:flags]} converge #{args[:opts]} 2>&1 | tee -a #{testout_fn}"
end
task :destroy,[:flags,:opts] do |task,args|
  sh "date '+%F-%X molecule test start' > #{testout_fn}"
  bash "molecule #{args[:flags]} destroy #{args[:opts]} 2>&1 | tee -a #{testout_fn}"
end
