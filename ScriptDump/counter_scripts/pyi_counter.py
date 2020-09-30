#!/usr/local/bin/python3.8

import ast
import sys
import os
from pprint import pprint

class Analyzer(ast.NodeVisitor):
    def __init__(self):        
      self.stats = {}

    def visit_FunctionDef(self, node):
      
      for arg in ast.iter_child_nodes(node.args):
         if hasattr(arg,'annotation') and arg.annotation != None:
           #print("arg with annotation: ",arg,self._interpret(arg.annotation));
           self.stats[node.name+"."+arg.arg] = arg.annotation;
           #pprint(ast.dump(arg, include_attributes=True));

      if hasattr(node,'returns') and node.returns != None:
        #print("RETURN with annotation: ",node.returns,self._interpret(node.returns));
        self.stats[node.name+".return"] = node.returns;
        #pprint(ast.dump(node, include_attributes=True));        

      super(Analyzer, self).generic_visit(node);

    def visit_AnnAssign(self, node):
        # AnnAssign has target, annotation, and value attributes. 
        if hasattr(node,'annotation') and node.annotation != None: 
          if hasattr(node,'target') and hasattr(node.target,'id'):
            self.stats[node.target.id] = node.annotation;
          else: 
            print("WRONG SYNTAX: the AnnAssign thing...",node,interpret(node.annotation));          
            pprint(ast.dump(node, include_attributes=True));

        super(Analyzer, self).generic_visit(node);

    def report(self):
        pprint(self.stats)

def interpret(node):
      if (isinstance(node,ast.Name)):
         return node.id
      elif (isinstance(node,ast.Subscript)):
         name = interpret(node.value);
         index = interpret(node.slice);
         return name+'['+index+']';
      elif (isinstance(node,ast.Index)):
         return interpret(node.value);
      elif (isinstance(node,ast.Tuple)):
         result = '';
         for elem in node.elts:
           result = result+',' + interpret(elem)
         return result[1:]
      elif (isinstance(node,ast.Constant)):
         if node.value==None:
           return "None"
         else:
           return str(node.value)
      elif (isinstance(node,ast.Attribute)):
         # Attribute := Attribute.str Attribute is field value, str is field "attr" which should be instance of str
         assert isinstance(node.attr,str),"Offending attribute: "+pprint(node);
         # return interpret(node.value)+"."+node.attr #TODO HACK to avoid type mismatch such as pathlib.Path vs. Path
         return node.attr
      else:
         return "Interpret: Malformed? "+str(node) #+ast.dump(node,include_attributes=True); TODO: This comes up with Callable but fairly few cases to warrent fix.

# assumes original_stats has the "ground set" of keys/vars that we are comparing over
def match(original_stats, stripped_stats):
   stats = { "EXACT match": 0, "EXACT match of Any": 0, "EXACT match of None": 0, "Top-level match": 0, "Option match": 0, "Any vs. other": 0, "Other vs. Any": 0, "Other": 0 }

   for key in original_stats.keys():
     if not(key in stripped_stats.keys()):
       stripped_stats[key] = ast.Name(id="Any"); # Fake Any for implicit/missing Any 

   #for key in stripped_stats.keys():
   #  if not(key in original_stats.keys()):
   #    original_stats[key] = ast.Name(id='Any');

   for key in original_stats.keys():
       orig_anno = original_stats[key];
       stripped_anno = stripped_stats[key];
       print("\n==== Key: ",key); 
       if interpret(orig_anno) == interpret(stripped_anno) and interpret(orig_anno) == 'Any':
          print('Exact match of Any: ',interpret(orig_anno),interpret(stripped_anno));
          stats['EXACT match of Any']+=1; 
       elif interpret(orig_anno) == interpret(stripped_anno) and interpret(orig_anno) == 'None':
          print('Exact match of None: ',interpret(orig_anno),interpret(stripped_anno));
          stats['EXACT match of None']+=1;
       elif interpret(orig_anno) == interpret(stripped_anno):
          print('Exact match: ',interpret(orig_anno),'=', interpret(stripped_anno)); 
          stats['EXACT match']+=1;
       elif 'Any' == interpret(stripped_anno):
          print('Other vs. ANY:', interpret(orig_anno), 'vs.', interpret(stripped_anno));
          stats['Other vs. Any']+=1;
       elif 'Any' == interpret(orig_anno):
          print('Any vs. other:', interpret(orig_anno), 'vs.', interpret(stripped_anno));
          stats['Any vs. other']+=1; 
       elif isinstance(orig_anno, ast.Subscript) and isinstance(stripped_anno, ast.Subscript) and interpret(orig_anno.value)==interpret(stripped_anno.value):
          print('TOP-LEVEL match: orig_anno == stripped_anno: ', interpret(orig_anno), 'vs.', interpret(stripped_anno));
          stats['Top-level match']+=1;
       elif (isinstance(stripped_anno,ast.Subscript) and interpret(stripped_anno.value)=='Optional' and interpret(stripped_anno.slice)==interpret(orig_anno)) or (isinstance(orig_anno,ast.Subscript) and interpret(orig_anno.value)=='Optional' and interpret(orig_anno.slice)==interpret(stripped_anno)):
          # original: Optional[type] vs stripped: Optional[type]                                              
          print('OPTIONAL match: ', interpret(orig_anno), 'vs.', interpret(stripped_anno));
          stats['Option match']+=1; 
       else:
          print('OTHER, no match: ', interpret(orig_anno), ' vs.', interpret(stripped_anno));
          stats['Other']+=1;

   pprint(stats);
   return stats;

def main(original, stripped):

   original_analyzer = Analyzer()

   try:
      with open(original, "r") as source:
         tree = ast.parse(source.read(), type_comments=True, feature_version=sys.version_info[1])
         original_analyzer.visit(tree);
   except SyntaxError:
      print("Oops, Syntax error?")                                                                                                                                                       

   stripped_analyzer = Analyzer()

   try:
      with open(stripped, "r") as source:
         tree = ast.parse(source.read(), type_comments=True, feature_version=sys.version_info[1])
         stripped_analyzer.visit(tree);
   except SyntaxError:
      print("Oops, Syntax error?")                                                                                                                                                       

   return match(original_analyzer.stats, stripped_analyzer.stats);

if __name__ == "__main__":

   pyi_data_root = "/Users/ana/Downloads/python3_types-master/Result/4079files/"
   
   total_stats = { "EXACT match": 0, "EXACT match of Any": 0, "EXACT match of None": 0, "Top-level match": 0, "Option match": 0, "Any vs. other": 0, "Other vs. Any": 0, "Other": 0 }
   
   num = 0;
   for root,dirs,files in os.walk(pyi_data_root):
     for original in files: 
       if original.endswith(".py"):
         original_full = os.path.join(pyi_data_root,'source_2/'+original);
         print('Processing original_full:', original_full);
         stripped = original[0:original.index('.')]+'-Stripped.pyi';
         stripped_full = os.path.join(pyi_data_root,'stripped_num/'+stripped); 
         print('Processing stripped_full:', stripped_full);
         stats = main(original_full,stripped_full)
         for key in stats.keys():
            total_stats[key] = total_stats[key] + stats[key];
         num = num + 1;

   print("\n\nTotal stats over", num, "files:");
   pprint(total_stats);
   total_vars = 0;
   for key in total_stats.keys():
     total_vars = total_vars+total_stats[key];

   percentage_totals = { "EXACT match": 0, "EXACT match of Any": 0, "EXACT match of None": 0, "Top-level match": 0, "Option match": 0, "Any vs. other": 0, "Other vs. Any": 0, "Other": 0 }

   for key in total_stats.keys():
     per_key = total_stats[key]/total_vars;
     percentage_totals[key] = "{:.2}".format(per_key);
   print("\nTotal % stats");
   pprint(percentage_totals);
