package learn.avinash.figaro.quicktutorial

import com.cra.figaro.algorithm.factored.VariableElimination
import com.cra.figaro.language.{Apply, Flip}

object ConstrainsSample {
  def main(args: Array[String]): Unit = {
    val result1 = Flip(0.4)
    val result2 = Flip(0.4)
    val result3 = Flip(0.4)

    val allWins = Apply(result1,result2,result3, (w1:Boolean, w2:Boolean,w3:Boolean) => w1 && w2 && w3)
    println(VariableElimination.probability(allWins, true))
  }

}
