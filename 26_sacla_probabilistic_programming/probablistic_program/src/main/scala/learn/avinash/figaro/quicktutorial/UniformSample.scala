package learn.avinash.figaro.quicktutorial

import com.cra.figaro.algorithm.sampling.Importance
import com.cra.figaro.library.atomic.continuous.Uniform

object UniformSample {

  val temperature = Uniform(10,70)
  def greaterThan50(d: Double) = d > 50

  def main(args: Array[String]): Unit = {
  println(Importance.probability(temperature, greaterThan50 _))
  }

}
