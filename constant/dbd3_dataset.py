# Docking Benchmark 3.0 (abbreviated as DBD3)
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2726780/
# List of PDB ID of protein complexes based on Complex Category Labels
# E = Enzyme-Inhibitor or Enzyme-Substrate
dbd3_e_list = [ # Rigid-body
               "1AVX", "1AY7", "1BVN", "1CGI", "1D6R", "1DFJ", "1E6E", "1EAW",
               "1EWY", "1EZU", "1F34", "1HIA", "1MAH", "1N8O", "1OPH", "1PPE",
               "1R0R", "1TMQ", "1UDI", "1YVB", "2B42", "2MTA", "2O8V", "2PCC",
               "2SIC", "2SNI", "2UUY", "7CEI",
                # Medium Difficulty
               "1ACB", "1IJK", "1KKL", "1M10", "1NW9",
                # Difficult
               "1FQ1", "1PXV"]

# A = Antibody-Antigen
dbd3_a_list = [ # Rigid-body
               "1AHW", "1BVK", "1DQJ", "1E6J", "1JPS", "1MLC", "1VFB", "1WEJ",
               "2FD6", "2I25", "2VIS",
                # Medium Difficulty
               "1BGX",
                # Difficult
               "1E4K"]

# AB = Antigen-Bound Antibody
dbd3_ab_list = [ # Rigid-body
                "1BJ1", "1FSK", "1I9R", "1IQD", "1K4C", "1KXQ", "1NCA", "1NSN",
                "1QFW", "2JEL",
                 # Difficult
                "2HMI"]

# O = Others
dbd3_o_list = [ # Rigid-body
                "1A2K", "1AK4", "1AKJ", "1AZS", "1B6C", "1BUH", "1E96", "1EFN",
                "1F51", "1FC2", "1FQJ", "1GCQ", "1GHQ", "1GLA", "1GPW", "1HE1",
                "1I4D", "1J2J", "1K74", "1KAC", "1KLU", "1KTZ", "1KXP", "1ML0",
                "1QA9", "1RLB", "1S1Q", "1SBB", "1T6B", "1XD3", "1Z0K", "1Z5Y",
                "1ZHI", "2AJF", "2BTF", "2HLE", "2HQS", "2OOB",
                # Medium Difficulty
                "1GP2", "1GRN", "1HE8", "1I2M", "1IB1", "1K5D", "1N2C", "1WQ1",
                "1XQS", "2CFH", "2H7V", "2HRK", "2NZ8",
                # Difficult
                "1ATN", "1BKD", "1DE4", "1EER", "1FAK", "1H1V", "1IBR", "1IRA", "1JMO",
                "1R8S", "1Y64", "2C0L", "2OT3"]

dbd3_all_list = dbd3_e_list + dbd3_a_list + dbd3_ab_list + dbd3_o_list
