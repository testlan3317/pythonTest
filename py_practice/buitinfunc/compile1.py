x = compile('print(55)', 'test', 'eval')
exec(x)

# source - Required: The source to compile, can be a String, a Byte object, or an AST object
# filename - Required
#  The name of the file that the source comes from. If the source does not come from a file, you can write whatever you like 
# mode - Required
#    eval - if the source is a sigle expression
#    exec - if the source is a block of statements
#    single - if the source is a single interactive statement
