#!/usr/bin/env ruby

require 'rubygems'
require 'optparse'
require 'elasticsearch'

options = {}

opts_parser = OptionParser.new do |opts|
  opts.banner = "Usage: elasticsearch_stats.rb [options]"

  opts.on("-i SERVER", "--ip SERVER", String, "Server IP to check") do |server|
    options[:ip] = server
  end

  opts.on("-p PORT", "--port PORT", Integer, "Port to use to connect to server, default 9200") do |port|
    options[:port] = port
  end

  opts.on("-h", "--help", "Display this screen" ) do
    puts opts
    exit 3
  end

end

opts_parser.parse!
mandatory = [:ip]
missing = mandatory.select{ |param| options[param].nil? }
if not missing.empty?
  puts "Missing options: #{missing.join(', ')}"
  puts opts_parser
  exit 3
end

options[:port] = 9200 if options[:port].nil?

client = Elasticsearch::Client.new({:hosts => [options[:ip] + ':' + options[:port].to_s]})

node_stats = client.nodes.stats({:node_id => options[:ip]})
node_id = node_stats['nodes'].keys[0]

stats = Hash.new
stats['indeces_docs_count'] = node_stats['nodes'][node_id]['indices']['docs']['count']
stats['indeces_docs_deleted'] = node_stats['nodes'][node_id]['indices']['docs']['deleted']
stats['indeces_store_size'] = node_stats['nodes'][node_id]['indices']['store']['size_in_bytes']
stats['indexing_index_total'] = node_stats['nodes'][node_id]['indices']['indexing']['index_total']
stats['indexing_index_time'] = node_stats['nodes'][node_id]['indices']['indexing']['index_time_in_millis']
stats['indexing_delete_total'] = node_stats['nodes'][node_id]['indices']['indexing']['delete_total']
stats['indexing_delete_time'] = node_stats['nodes'][node_id]['indices']['indexing']['delete_time_in_millis']
stats['get_total'] = node_stats['nodes'][node_id]['indices']['get']['total']
stats['get_time'] = node_stats['nodes'][node_id]['indices']['get']['time_in_millis']
stats['get_exists_total'] = node_stats['nodes'][node_id]['indices']['get']['exists_total']
stats['get_exists_time'] = node_stats['nodes'][node_id]['indices']['get']['exists_time_in_millis']
stats['get_missing_total'] = node_stats['nodes'][node_id]['indices']['get']['missing_total']
stats['get_missing_time'] = node_stats['nodes'][node_id]['indices']['get']['missing_time_in_millis']
stats['search_query_total'] = node_stats['nodes'][node_id]['indices']['search']['query_total']
stats['search_query_time'] = node_stats['nodes'][node_id]['indices']['search']['query_time_in_millis']
stats['search_fetch_total'] = node_stats['nodes'][node_id]['indices']['search']['fetch_total']
stats['search_fetch_time'] = node_stats['nodes'][node_id]['indices']['search']['fetch_time_in_millis']
stats['merges_total'] = node_stats['nodes'][node_id]['indices']['merges']['total']
stats['merges_time'] = node_stats['nodes'][node_id]['indices']['merges']['total_time_in_millis']
stats['merges_total_docs'] = node_stats['nodes'][node_id]['indices']['merges']['total_docs']
stats['merges_total_size'] = node_stats['nodes'][node_id]['indices']['merges']['total_size_in_bytes']
stats['refresh_total'] = node_stats['nodes'][node_id]['indices']['refresh']['total']
stats['refresh_total_time'] = node_stats['nodes'][node_id]['indices']['refresh']['total_time_in_millis']
stats['flush_total'] = node_stats['nodes'][node_id]['indices']['flush']['total']
stats['flush_total_time'] = node_stats['nodes'][node_id]['indices']['flush']['total_time_in_millis']
stats['warmer_total'] = node_stats['nodes'][node_id]['indices']['warmer']['total']
stats['warmer_total_time'] = node_stats['nodes'][node_id]['indices']['warmer']['total_time_in_millis']
stats['filter_cache_mem_size'] = node_stats['nodes'][node_id]['indices']['filter_cache']['memory_size_in_bytes']
stats['id_cache_mem_size'] = node_stats['nodes'][node_id]['indices']['id_cache']['memory_size_in_bytes']
stats['fielddata_mem_size'] = node_stats['nodes'][node_id]['indices']['fielddata']['memory_size_in_bytes']
stats['completion_size'] = node_stats['nodes'][node_id]['indices']['completion']['size_in_bytes']
stats['segments'] = node_stats['nodes'][node_id]['indices']['segments']['count']
stats['process_open_files'] = node_stats['nodes'][node_id]['process']['open_file_descriptors']
stats['process_cpu_percent'] = node_stats['nodes'][node_id]['process']['cpu']['percent']
stats['process_cpu_sys'] = node_stats['nodes'][node_id]['process']['cpu']['sys_in_millis']
stats['process_cpu_user'] = node_stats['nodes'][node_id]['process']['cpu']['user_in_millis']
stats['process_cpu_total'] = node_stats['nodes'][node_id]['process']['cpu']['total_in_millis']
stats['process_mem_resident'] = node_stats['nodes'][node_id]['process']['mem']['resident_in_bytes']
stats['process_mem_share'] = node_stats['nodes'][node_id]['process']['mem']['share_in_bytes']
stats['process_mem_virtual'] = node_stats['nodes'][node_id]['process']['mem']['total_virtual_in_bytes']
stats['jvm_uptime'] = node_stats['nodes'][node_id]['jvm']['uptime_in_millis']
stats['jvm_mem_heap_used'] = node_stats['nodes'][node_id]['jvm']['mem']['heap_used_in_bytes']
stats['jvm_mem_heap_committed'] = node_stats['nodes'][node_id]['jvm']['mem']['heap_committed_in_bytes']
stats['jvm_mem_heap_max'] = node_stats['nodes'][node_id]['jvm']['mem']['heap_max_in_bytes']
stats['jvm_mem_non_heap_used'] = node_stats['nodes'][node_id]['jvm']['mem']['non_heap_used_in_bytes']
stats['jvm_mem_non_heap_committed'] = node_stats['nodes'][node_id]['jvm']['mem']['non_heap_committed_in_bytes']
stats['jvm_threads'] = node_stats['nodes'][node_id]['jvm']['threads']['count']

out_string = ""
stats.each{|name, value| out_string = out_string + name + ':' + value.to_s + ' ' }

puts out_string
