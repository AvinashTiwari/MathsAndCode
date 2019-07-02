import com.cra.figaro.algorithm.factored.VariableElimination
import com.cra.figaro.language._

object firstmodel {

  def main(args: Array[String]): Unit = {
    val sunnyToday = Flip(0.2)
    println(VariableElimination.apply(sunnyToday))
  }

}
