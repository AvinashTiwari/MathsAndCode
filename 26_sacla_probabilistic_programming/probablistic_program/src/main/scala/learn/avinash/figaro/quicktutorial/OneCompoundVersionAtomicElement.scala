package learn.avinash.figaro.quicktutorial

import com.cra.figaro.algorithm.sampling.Importance
import com.cra.figaro.language.{Flip, Select}
import com.cra.figaro.library.atomic.continuous.{Normal, Uniform}

object OneCompoundVersionAtomicElement {

  def main(args: Array[String]): Unit = {
    val sunnyTodayProb = Uniform(0,0.5)
    val sunnyToday = Flip(sunnyTodayProb);
    println(Importance.probability(sunnyToday,true))

    val tempMean = Normal(40,9)
    val temperature = Normal(tempMean,100)
    println(Importance.probability(temperature,(d:Double)=> d >50))


    val tempMeanNew = Normal(40,9)
    val tempVariance = Select(0.5 -> 80.0, 0.5 -> 105.0)
    val temperatureNew =Normal(tempMeanNew, tempVariance)
    println(Importance.probability(temperatureNew, (d:Double)=> d >50))

  }

}
