# The MIT License
#
# Copyright (c) 2017 Eugene Chekanskiy, echekanskiy@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import time

from hvapi.clr.types import Msvm_ConcreteJob_JobState, VSMS_ModifyResourceSettings_ReturnCode, \
  VSMS_ModifySystemSettings_ReturnCode, VSMS_AddResourceSettings_ReturnCode
from hvapi.clr.base import JobException, ManagementObject
from hvapi.clr.invoke import evaluate_invocation_result


class MOWrapper(ManagementObject):
  def __init__(self, mo: ManagementObject, parent: 'MOWrapper' = None):
    self.Path = mo.Path
    self.check_class(self.MO_CLS)
    self.parent = parent


class JobWrapper(MOWrapper):
  MO_CLS = ('Msvm_ConcreteJob', 'Msvm_StorageJob')

  def wait(self):
    job_state = Msvm_ConcreteJob_JobState.from_code(self.properties['JobState'])
    while job_state not in [Msvm_ConcreteJob_JobState.Completed, Msvm_ConcreteJob_JobState.Terminated,
                            Msvm_ConcreteJob_JobState.Killed, Msvm_ConcreteJob_JobState.Exception]:
      job_state = Msvm_ConcreteJob_JobState.from_code(self.properties['JobState'])
      self.reload()
      time.sleep(.1)
    if job_state != Msvm_ConcreteJob_JobState.Completed:
      raise JobException(self)


class VirtualSystemManagementService(MOWrapper):
  MO_CLS = 'Msvm_VirtualSystemManagementService'

  def SetGuestNetworkAdapterConfiguration(self, ComputerSystem, *args):
    out_objects = self.invoke("SetGuestNetworkAdapterConfiguration", ComputerSystem=ComputerSystem,
                              NetworkConfiguration=args)
    return evaluate_invocation_result(
      out_objects,
      VSMS_ModifyResourceSettings_ReturnCode,
      VSMS_ModifyResourceSettings_ReturnCode.Completed_with_No_Error,
      VSMS_ModifyResourceSettings_ReturnCode.Method_Parameters_Checked_Job_Started
    )

  def ModifyResourceSettings(self, *args):
    out_objects = self.invoke("ModifyResourceSettings", ResourceSettings=args)
    return evaluate_invocation_result(
      out_objects,
      VSMS_ModifyResourceSettings_ReturnCode,
      VSMS_ModifyResourceSettings_ReturnCode.Completed_with_No_Error,
      VSMS_ModifyResourceSettings_ReturnCode.Method_Parameters_Checked_Job_Started
    )

  def ModifySystemSettings(self, SystemSettings):
    out_objects = self.invoke("ModifySystemSettings", SystemSettings=SystemSettings)
    return evaluate_invocation_result(
      out_objects,
      VSMS_ModifySystemSettings_ReturnCode,
      VSMS_ModifySystemSettings_ReturnCode.Completed_with_No_Error,
      VSMS_ModifySystemSettings_ReturnCode.Method_Parameters_Checked_Job_Started
    )

  def AddResourceSettings(self, AffectedConfiguration, *args):
    out_objects = self.invoke("AddResourceSettings", AffectedConfiguration=AffectedConfiguration, ResourceSettings=args)
    return evaluate_invocation_result(
      out_objects,
      VSMS_AddResourceSettings_ReturnCode,
      VSMS_AddResourceSettings_ReturnCode.Completed_with_No_Error,
      VSMS_AddResourceSettings_ReturnCode.Method_Parameters_Checked_Job_Started
    )

  def DefineSystem(self, SystemSettings, ResourceSettings=[], ReferenceConfiguration=None):
    out_objects = self.invoke("DefineSystem", SystemSettings=SystemSettings, ResourceSettings=ResourceSettings,
                              ReferenceConfiguration=ReferenceConfiguration)
    return evaluate_invocation_result(
      out_objects,
      VSMS_AddResourceSettings_ReturnCode,
      VSMS_AddResourceSettings_ReturnCode.Completed_with_No_Error,
      VSMS_AddResourceSettings_ReturnCode.Method_Parameters_Checked_Job_Started
    )
