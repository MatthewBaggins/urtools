# To restore in later versions (maybe?)
# def issubtype(sub: type, 
#               sup: Union[type, tuple[type, tuple[type, ...], ...]]
#               ) -> bool:
#     """Check whether the type `sub` properly narrows down the type (or tuple of types) `sup`.
#     """
    
#     if isinstance(sup, tuple):
#         return any(issubtype(sub, sup_) for sup_ in sup)
    
#     # The most basic case
#     if not (isinstance(sub, GenericAlias) or isinstance(sup, GenericAlias)
#         ) and issubclass(sub, sup):
#         return True
    
#     # If `sub` and `sup` were not created using the same functor`
#     if get_origin(sub) != get_origin(sup):
#         return False
        
#     sup_args = get_args(sup)
#     sub_args = get_args(sub)

#     if sup_args == sub_args == ():
#         return False

#     if all(
#         any( issubtype(sub_arg, sup_arg) for sup_arg in sup_args
#             ) for sub_arg in sub_args):
#         return True
    
#     return False