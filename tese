adadasdasdsdfdfsda
ef config = new HashMap()
def bindings = getBinding()
config.putAll(bindings.getVariables())
def out = config['out']
  jenkins.model.Jenkins.instance.getComputers().each { computer ->
  // check if executor is dead
  execList = computer.getExecutors()
  println(execList)
  execlist = 
  for( exec in execList ) {
    if (exec.getCauseOfDeath()) {
      println("\tNode: ${computer.getDisplayName()}, executer ${exec.getDisplayName()} is dead.")
      println("Error:")
      exec.getCauseOfDeath().printStackTrace(out) 
      println('\n')
      println("\tRemoving Dead Executor.")
      exec.doYank()
    }
  }
}
