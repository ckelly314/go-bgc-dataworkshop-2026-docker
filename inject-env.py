import os

renviron_path = os.path.expanduser('~/.Renviron')

# Capture specific environment variables from the container
vars_to_capture = ['PATH', 'RETICULATE_PYTHON'] + [k for k in os.environ.keys() if k.startswith('AWS_')]

with open(renviron_path, 'a') as f:
    f.write('\n# Environment variables from container\n')
    for key in sorted(vars_to_capture):
        if key in os.environ:
            value = os.environ[key]
            # Escape quotes and newlines
            escaped_value = value.replace('"', '\\"').replace('\n', '\\n')
            f.write(f'{key}="{escaped_value}"\n')
