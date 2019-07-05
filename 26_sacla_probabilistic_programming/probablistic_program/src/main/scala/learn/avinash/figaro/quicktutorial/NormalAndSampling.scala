package learn.avinash.figaro.quicktutorial
import com.cra.figaro.algorithm.sampling.Importance
import com.cra.figaro.library.atomic.continuous.Normal
object NormalAndSampling {
  val temperature = Normal(40,100)
  def greaterThan50(d: Double) = d > 50

  def main(args: Array[String]): Unit = {
    println(Importance.probability(temperature, greaterThan50 _))
  }

}
