import yaml
import objectTypes
import datafiles
import path

class AnObject():
    typ = 0

    def __init__(self, typ):
        self.typ = typ

class ObjectsFactory():

    objectsFilename = datafiles.objects

    def __init__(self):
        self.load()

    def load(self):
        """ Load objects prototypes. """
        self.objetcsPrototypes = yaml.load(open(path.getPath(self.objectsFilename)))

    def createObject(self, name):
        if name in self.objetcsPrototypes:
            objectModel = self.objetcsPrototypes[name]
            obj = AnObject(objectModel['typ'])
            for propname, propvalue in objectModel.items():
                setattr(obj, propname, propvalue)
            return obj
        return False

if __name__=='__main__':
    factory = ObjectsFactory()
    ob1 = factory.createObject('apple')
    print(ob1, ob1.typ, ob1.imagename, ob1.basePrice)
