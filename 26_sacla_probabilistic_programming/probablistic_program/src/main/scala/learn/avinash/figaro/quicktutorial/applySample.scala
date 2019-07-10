package learn.avinash.figaro.quicktutorial

import com.cra.figaro.algorithm.factored.VariableElimination
import com.cra.figaro.language.Apply
import com.cra.figaro.library.atomic.discrete.Binomial

object applySample {
  def getQtly(i:Int):String = if(i > 10) "Good"; else if(i >5 ) "average"; else "Poor"
  def main(args: Array[String]): Unit = {
    val numSunnyDaysInWeek = Binomial(30,0.2)


    val MonthQtly = Apply(numSunnyDaysInWeek,getQtly)
    println(VariableElimination.probability(MonthQtly, "Good"))

  }

}
