
line = 'Failed login for root from 10.0.0.9'

print(line.startswith('Failed')) # Ouput: True
print(line.endswith('9'))        # Output: True

print(line.replace('root', 'REDACTED'))
# Ouput: Failed login for REDACTED from 10.0.0.9


# Ouput:
# True                                                                                                            
# True                                                                                                            
# Failed login for REDACTED from 10.0.0.9
