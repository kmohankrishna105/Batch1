str1="Welcome to the session"
lang=['python','Java','pearl']


assert 'Welcome to the session'== str1 , "Both strings are not matching"
print("Success")
print("Success2")
# asser condition(expected==actual, "message to be displayed"

verify_obj='pearl'
assert verify_obj in lang ,f"Lang is not having that value -{verify_obj}"
print("ruby is present")

#dictionary validation
lang_dict={1:'python',2:'pearl',3:'java'}
assert 'ruby' in lang_dict.values(),"Dict is not having the values"