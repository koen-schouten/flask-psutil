def string_in_strings(valid_string_list):
    def inner_func(str):
        return str.lower() in valid_string_list
    return inner_func
    
true_strings = ['true', '1']
string_is_true = string_in_strings(true_strings)

false_strings = ['false', '0']
string_is_false = string_in_strings(false_strings)

valid_connection_kinds = ["inet", "inet4", "inet6" "tcp",
                          "tcp4", "tcp6", "udp", "udp4", "udp6", "unix", "all"]
is_valid_connection_kind = string_in_strings(valid_connection_kinds)

valid_attrs = ['cmdline', 'connections', 'cpu_affinity', 'cpu_num', 'cpu_percent', 'cpu_times', 'create_time', 'cwd', 'environ', 'exe', 'gids', 'io_counters', 'ionice', 'memory_full_info', 'memory_info',
               'memory_maps', 'memory_percent', 'name', 'nice', 'num_ctx_switches', 'num_fds', 'num_handles', 'num_threads', 'open_files', 'pid', 'ppid', 'status', 'terminal', 'threads', 'uids', 'username']
is_valid_attrs = string_in_strings(valid_attrs)