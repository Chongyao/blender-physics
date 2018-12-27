discrete_method = (
    ('METHOD_FEM', 'fem', 'finte element method'),
    ('METHOD_MASS_SPRING', 'mass_spring', 'mass spring method'),
    ('METHOD_MESHLESS', 'meshless', 'meshless method')
)
#(para_name, data_type, if exposed, (Enum))
fem_parameter = ()
mass_spring_parameter = (('stiffness', 'float', True))
meshless_parameter = ()
