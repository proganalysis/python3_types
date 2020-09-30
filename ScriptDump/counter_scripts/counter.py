#!/usr/local/bin/python3.8

import ast
import sys
import os
import string
from pprint import pprint

from data import built_in_types

class Analyzer(ast.NodeVisitor):
    def __init__(self):        
      #self.stats = {"None": 0, "Any": 0, "List": 0, "Dict": 0, "Tuple": 0, "Optional": 0, "Set": 0, "Union": 0, "Built-in composite": 0,
      #              "Built-in base": 0, "int": 0, "float": 0, "str": 0, "complex": 0, "bytes": 0, "bool": 0, "dict": 0, "list": 0, "set": 0,
      #              "object": 0, "tuple": 0, "malformed": 0,
      #              "User-defined generic": [], "User-defined non-generic": [] }
      self.stats = {"None": 0, "Any": 0, "List": 0, "Dict": 0, "Tuple": 0, "Set": 0, "Optional": 0, "Union": 0, "Callable": 0,
                    "int": 0, "float": 0, "str": 0, "complex": 0, "bytes": 0, "bool": 0, "list": 0, "dict": 0, "tuple": 0,
                    "set": 0, "object": 0, "malformed": 0, "Built-in": 0,
                    "User-defined": 0 }
      self.params = {"None": 0, "Any": 0, "List": 0, "Dict": 0, "Tuple": 0, "Set": 0, "Optional": 0, "Union": 0, "Callable": 0,
                     "int": 0, "float": 0, "str": 0, "complex": 0, "bytes": 0, "bool": 0, "list": 0, "dict": 0, "tuple": 0,
                     "set": 0, "object": 0, "malformed": 0, "Built-in": 0,
                     "User-defined": 0 }
      self.returns = {"None": 0, "Any": 0, "List": 0, "Dict": 0, "Tuple": 0, "Set": 0, "Optional": 0, "Union": 0, "Callable": 0,
                     "int": 0, "float": 0, "str": 0, "complex": 0, "bytes": 0, "bool": 0, "list": 0, "dict": 0, "tuple": 0,
                     "set": 0, "object": 0, "malformed": 0, "Built-in": 0,
                     "User-defined": 0 }

    def _interpret(self,node):
      if (isinstance(node,ast.Name)):
         return node.id
      elif (isinstance(node,ast.Subscript)):
         name = self._interpret(node.value);
         index = self._interpret(node.slice);
         return name+'['+index+']';
      elif (isinstance(node,ast.Index)):
         return self._interpret(node.value);       
      elif (isinstance(node,ast.Tuple)):
         result = '';
         for elem in node.elts:
           result = result+',' + self._interpret(elem)
         return result[1:]
      elif (isinstance(node,ast.Constant)):
         if node.value==None: 
           return "None"
         else: 
           return node.value
      else:
         return "Interpret: Malformed? "+str(node) #+ast.dump(node,include_attributes=True);

    def _classify(self, anno_string, composite, is_param, is_return):
      if (anno_string in self.stats.keys()):
         self.stats[anno_string] += 1; 
         if is_param: self.params[anno_string] += 1;
         if is_return: self.returns[anno_string] += 1;
      elif (anno_string in built_in_types and composite == True):
         self.stats['Built-in'] += 1;
         if is_param: self.params['Built-in'] += 1;
         if is_return: self.returns['Built-in'] += 1; 
      elif (anno_string in built_in_types):
         self.stats['Built-in'] += 1;
         if is_param: self.params['Built-in'] += 1;
         if is_return: self.returns['Built-in'] += 1; 
      elif (composite==True):
         self.stats['User-defined'] += 1;  #.append(anno_string);
         if is_param: self.params['User-defined'] += 1;
         if is_return: self.returns['User-defined'] += 1;
      else:
         self.stats['User-defined'] += 1;  #.append(anno_string);
         if is_param: self.params['User-defined'] += 1;
         if is_return: self.returns['User-defined'] += 1;
    
    def _process_annotation(self, anno, is_param, is_return):
      if (anno==None): 
        return;
      if (isinstance(anno,ast.Name)): # typical case, str, int, bool
        self._classify(anno.id,False, is_param, is_return);
      elif (isinstance(anno,ast.Subscript) and isinstance(anno.value,ast.Name)): # typical case: List[...] Name refers to List.        
        self._classify(anno.value.id,True, is_param, is_return);
      elif (isinstance(anno,ast.Subscript) and isinstance(anno.value,ast.Attribute)): # covers the case typing.List[...] so value is Attribute
        # WARNING: Line numbers and offset may be incorrect on rare occasions
        new_sub = ast.Subscript(ast.Name(id=anno.value.attr, ctx=anno.value.ctx, lineno=anno.value.lineno, col_offset=anno.value.value.end_col_offset+1, 
                                               end_lineno=anno.value.lineno, end_col_offset=anno.value.end_col_offset),  
                                      anno.slice, ctx=anno.ctx, lineno=anno.lineno, col_offset=anno.value.value.end_col_offset+1, 
                                      end_lineno=anno.end_lineno, end_col_offset=anno.end_col_offset);
        # print("\nTESTING old Sub: ",ast.dump(anno, include_attributes=True)); 
        # print("NEW Sub: ",ast.dump(new_sub, include_attributes=True));        
        assert isinstance(new_sub.value,ast.Name);
        # self._classify(new_sub.value.id,True);
        self._process_annotation(new_sub, is_param, is_return);
      elif (isinstance(anno,ast.Attribute)): # and isinstance(anno.value,ast.Name)): # covers package.attr delcarations??? Anything possible in Python
        new_name = ast.Name(id=anno.attr, ctx=anno.ctx, lineno=anno.lineno, col_offset=anno.value.end_col_offset+2, # need to offset . 
                                 end_lineno=anno.end_lineno, end_col_offset=anno.end_col_offset)
        # print("\nTESTING old Sub: ",ast.dump(anno, include_attributes=True));   
        # print("NEW Name: ",ast.dump(new_name, include_attributes=True));  
        # print();
        self._process_annotation(new_name,is_param,is_return);
      elif (isinstance(anno,ast.Constant)):
        self._classify("None",False,is_param,is_return);
      else:
        # Things like: urlstr(x=something), or a tuple (str,int) or List[str] or None
        # Basically, not using proper syntax for Callable[], Union[], or Option[]
        print("Malformed annotation: ",ast.dump(anno));
        self._classify("malformed",False,is_param,is_return);

    def _process_type_comment(self, node, comment):
      #TODO
      pass

    def visit_FunctionDef(self, node):
      if hasattr(node, 'type_comment'):
        self._process_type_comment(node,node.type_comment);
      
      for arg in ast.iter_child_nodes(node.args):
         if hasattr(arg,'annotation') and arg.annotation != None:
           #print("arg with annotation: ",arg,self._interpret(arg.annotation));
           self._process_annotation(arg.annotation,True,False);
           #pprint(ast.dump(arg, include_attributes=True));

      if hasattr(node,'returns') and node.returns != None:
        #print("RETURN with annotation: ",node.returns,self._interpret(node.returns));
        self._process_annotation(node.returns,False,True); 
        
      super(Analyzer, self).generic_visit(node);

    def visit_AnnAssign(self, node):
        # AnnAssign has target, annotation and value attributes. 
        if hasattr(node, 'type_comment'):
          self._process_type_comment(node,node.type_comment);

        if hasattr(node,'annotation') and node.annotation != None: 
          #print("the AnnAssign thing...",node,self._interpret(node.annotation));
          self._process_annotation(node.annotation,False,False)
        #pprint(ast.dump(node, include_attributes=True));  

        super(Analyzer, self).generic_visit(node);
    
    def _report(self,stats):      
      for key in stats.keys():
           if isinstance(stats[key],int):
             print(key,":",stats[key]);
           else:
             print(key,":",len(stats[key]));
      key_string = ''; 
      results_string = '';
      for key in stats.keys():
         key_string += key+'\t'
         if isinstance(stats[key],int):
           results_string += str(stats[key])+'\t';
         else:
           results_string += str(len(stats[key]))+'\t';
      print(key_string);
      print(results_string); 

    def report(self):
        #pprint(self.stats)
        print("\n\nNumerical stats _all_:");
        self._report(self.stats);
        print("\n\nNumerical stats _params_:");
        self._report(self.params);
        print("\n\nNumerical stats _returns_:");
        self._report(self.returns);


analyzer = Analyzer();

def main(argv):

  for root,dirs,files in os.walk(argv):
    for file in files:
      if file.endswith(".py"):
        try: 
          #print("Opening file: ", os.path.join(root,file));
          with open(os.path.join(root,file), "r") as source:
            tree = ast.parse(source.read(), type_comments=True, feature_version=sys.version_info[1])
          analyzer.visit(tree);
        except SyntaxError:
          #print("Oops, Syntax error?")
          pass 
   
#  analyzer.report()  

if __name__ == "__main__":
   archive_root = "/Users/ana/Downloads/PythonRepoArchive"
   typed_repos_file = sys.argv[1]
   num_repos=0;
   for line in open(typed_repos_file, "r").readlines():
     s_line = line.strip()
     s_line = str.split(s_line)[3];
 
     org = s_line[1:s_line.index(')')]
     repo = s_line[s_line.index(')')+1:]
     repo_is_here = archive_root+'/'+org+'/'+repo;
     num_repos = num_repos + 1;
     print("\n",num_repos," repo is here:",repo_is_here);
     main(repo_is_here)
     print("Done with ",num_repos);
     #if num_repos > 10: break;
   analyzer.report();
