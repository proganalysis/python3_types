#!/usr/local/bin/python3.8

import ast
import sys
import os
import string
from pprint import pprint

from data import built_in_types

write_path = "/home/bew/Desktop/wp2/counter_scripts/raw"
fpWrite = open(write_path, 'w')
wwrite = False

class Analyzer(ast.NodeVisitor):
    def __init__(self):        
      self.num_anno = 0;
      self.num_files = 0;
      self.num_anno_per_file = 0;

    def visit_FunctionDef(self, node):
      #if hasattr(node, 'type_comment'):
      #  self._process_type_comment(node,node.type_comment);
      
      for arg in ast.iter_child_nodes(node.args):
         if hasattr(arg,'annotation') and arg.annotation != None:
           # print("arg with annotation: ",arg,arg.annotation);
           self.num_anno += 1;
           self.num_anno_per_file += 1;
           # pprint(ast.dump(arg, include_attributes=True));

      if hasattr(node,'returns') and node.returns != None:
        # print("RETURN with annotation: ",node.returns,node.returns);
        self.num_anno += 1;
        self.num_anno_per_file += 1;
        # pprint(ast.dump(node, include_attributes=True));
        
      super(Analyzer, self).generic_visit(node);

    def visit_AnnAssign(self, node):
        # AnnAssign has target, annotation and value attributes. 
        # if hasattr(node, 'type_comment'):
        # self._process_type_comment(node,node.type_comment);

        if hasattr(node,'annotation') and node.annotation != None: 
          # print("the AnnAssign thing...",node,node.annotation);
          self.num_anno += 1;
          self.num_anno_per_file += 1;
          # pprint(ast.dump(node, include_attributes=True));  

        super(Analyzer, self).generic_visit(node);
    
    def report(self):
        #pprint(self.stats)
        print("Stats: (",self.org,")",self.repo,"num_anno:",self.num_anno,",num_files:",self.num_files);
        if wwrite:
          oo = "(" + org + ")" + repo + ":" + str(self.num_anno) + ":" + str(self.num_files)
          fpWrite.write("=====\n%s\n" % oo)
        print("Histogram: ");
        for i in self.histogram.keys():
          print(i,":",self.histogram[i]);
          if wwrite:
            oo = str(i) + ":" + str(self.histogram[i])
            fpWrite.write("%s\n" % oo)

#analyzer = Analyzer();

def main(argv,org,repo):

  analyzer = Analyzer();
  analyzer.org = org;
  analyzer.repo = repo;
  analyzer.histogram = {};

  for root,dirs,files in os.walk(argv):
    for file in files:
      if file.endswith(".py"):
        try: 
          #print("Opening file: ", os.path.join(root,file));
          with open(os.path.join(root,file), "r") as source:
            tree = ast.parse(source.read(), type_comments=True, feature_version=sys.version_info[1])
          analyzer.num_anno_per_file = 0;  
          analyzer.visit(tree);
          analyzer.num_files += 1;
          if str(analyzer.num_anno_per_file) in analyzer.histogram.keys():
            analyzer.histogram[str(analyzer.num_anno_per_file)] += 1;
          else:
            analyzer.histogram[str(analyzer.num_anno_per_file)] = 1;
        except SyntaxError:
          #print("Oops, Syntax error?")
          pass 
  analyzer.report(); 

if __name__ == "__main__":
   #archive_root = "/Users/ana/Downloads/PythonRepoArchive"
   archive_root = "/home/bew/archive/typed_project/"
   typed_repos_file = sys.argv[1]

   num_repos=0;
   for line in open(typed_repos_file, "r").readlines():
     s_line = line.strip()
     s_line = str.split(s_line)[3];
 
     org = s_line[1:s_line.index(')')]
     repo = s_line[s_line.index(')')+1:]
     repo_is_here = archive_root+'/'+org+'/'+repo;
     
     repo_is_here = archive_root + s_line
     #print(repo_is_here)
     #exit()

     num_repos = num_repos + 1;
     print("\n",num_repos," repo is here:",repo_is_here);
     main(repo_is_here,org,repo)
     print("Done with ",num_repos);
     #if num_repos > 10: break;
   #analyzer.report();
