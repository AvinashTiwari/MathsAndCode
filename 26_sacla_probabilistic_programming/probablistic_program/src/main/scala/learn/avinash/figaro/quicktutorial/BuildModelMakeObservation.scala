package learn.avinash.figaro.quicktutorial

import com.cra.figaro.algorithm.factored.VariableElimination
import com.cra.figaro.language.{Flip, Select}
import com.cra.figaro.library.compound.If
object BuildModelMakeObservation {
  def main(args: Array[String]): Unit = {
    val sunnytoday = Flip(0.2)

    val greetingTodsy  = If(sunnytoday,
    Select (0.6 -> "Hello, world !", 0.4-> "Howdy Universe"),
    Select(0.2-> "Hello, world !", 0.8->"Oh no Not again"))

    greetingTodsy.observe("Hello, world !")

    println(VariableElimination.probability(sunnytoday, true))

    greetingTodsy.unobserve()

    println(VariableElimination.probability(sunnytoday, true))


    val sunnyTomorrow = If(sunnytoday, Flip(0.8), Flip(0.05))
    val greetingTomorrow  = If(sunnyTomorrow,
      Select (0.6 -> "Hello, world !", 0.4-> "Howdy Universe"),
      Select(0.2-> "Hello, world !", 0.8->"Oh no Not again"))


    println(VariableElimination.probability(greetingTomorrow, "Hello, world !"))
    greetingTodsy.observe("Hello, world !")


    println(VariableElimination.probability(greetingTomorrow, "Hello, world !"))
    greetingTomorrow.unobserve()



  }

}
