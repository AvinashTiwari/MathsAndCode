package learn.avinash.figaro.quicktutorial

import com.cra.figaro.algorithm.factored.VariableElimination
import com.cra.figaro.language.{Dist, Flip}

object DistSample {

  def main(args: Array[String]): Unit = {
    val goodMood = Dist(0.2 -> Flip(0.6), 0.8 -> Flip(0.2))
    println(VariableElimination.probability(goodMood,true))
  }

}
