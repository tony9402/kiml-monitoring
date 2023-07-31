
"""
    id => None
    uuid => id
    status => status
    run_name => name
    experiment_name => experiment_name
    image => image_name
    instance_type => resource_flavor
    create_time => ['system_meta']['createdAt']
    start_time => ['system_meta']['compute_started_at']
    end_time => ['system_meta']['compute_finished_at']
"""

def convert_run_dict(run_data):
    run_dict = {}
    
    uuid => id
    status => status
    run_name => name
    experiment_name => experiment_name
    image => image_name
    instance_type => resource_flavor
    create_time => ['system_meta']['createdAt']
    start_time => ['system_meta']['compute_started_at']
    end_time => ['system_meta']['compute_finished_at']