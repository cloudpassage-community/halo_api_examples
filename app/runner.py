import halo_api_examples


# Build config
config = halo_api_examples.ConfigHelper()

# get a halo object for api methods wrapper
halo = halo_api_examples.HaloGeneral(config)

halo_api_examples.HaloApiExamples(halo)
