import pandas as pd
import detecting_noise_functions as dnf

data=pd.read_csv('Number_of_Words_in_a_Language.csv')


print("Head Detection:")
a=dnf.add_distance_dict(data,5)
print(a[0],a[1])
print(dnf.detect_noise_head(dnf.add_distance_dict(data,5),500))

print("Head Detection:")
print(dnf.detect_noise_tail(dnf.add_distance_dict(data,5),500))