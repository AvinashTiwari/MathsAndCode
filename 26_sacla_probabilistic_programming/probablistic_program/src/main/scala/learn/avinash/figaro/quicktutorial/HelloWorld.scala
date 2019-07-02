package learn.avinash.figaro.quicktutorial
import  com.cra.figaro.language._
import com.cra.figaro.algorithm.factored.VariableElimination

object HelloWorld {
  def main(args: Array[String]): Unit = {
    val sunnytoday = Flip(0.2)
    println(VariableElimination.probability(sunnytoday,true))

  }

}
