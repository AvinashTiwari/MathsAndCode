package learn.avinash.figaro.quicktutorial
import com.cra.figaro.algorithm.factored.VariableElimination
import com.cra.figaro.library.atomic.discrete.Binomial

object BioNomial {
  def main(args: Array[String]): Unit = {
    val numSunnyDaysInWeek = Binomial(7,0.2)
    println(VariableElimination.probability(numSunnyDaysInWeek, 3))

  }
}
