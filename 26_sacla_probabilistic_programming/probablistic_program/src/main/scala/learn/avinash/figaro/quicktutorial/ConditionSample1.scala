package learn.avinash.figaro.quicktutorial

import com.cra.figaro.algorithm.factored.VariableElimination
import com.cra.figaro.library.atomic.discrete.Binomial

object ConditionSample1 {
  def main(args: Array[String]): Unit = {
    val sunnyDaysInMonth = Binomial(30,0.2)
    println(VariableElimination.probability(sunnyDaysInMonth,5))
    sunnyDaysInMonth.setCondition((i: Int) => i > 8)
    println(VariableElimination.probability(sunnyDaysInMonth,5))

  }

}
