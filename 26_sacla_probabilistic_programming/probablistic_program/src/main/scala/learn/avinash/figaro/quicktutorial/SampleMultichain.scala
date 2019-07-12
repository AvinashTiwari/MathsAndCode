package learn.avinash.figaro.quicktutorial

import com.cra.figaro.algorithm.factored.VariableElimination
import com.cra.figaro.language.{Apply, Chain, Flip}
import com.cra.figaro.library.atomic.discrete.Binomial

object SampleMultichain {
  def main(args: Array[String]): Unit = {
    val sunnyToday = Flip(0.2)
    val numSunnyDaysInWeek = Binomial(30,0.2)

    val  teamWithInMonth = Binomial(5,0.4)
    val monthlyQlty = Apply(numSunnyDaysInWeek,teamWithInMonth, (days: Int, wins:Int) =>{
      val x = days * wins
      if( x > 20) "good"; else if(x >10) "average"; else "poor"
    } )


    val goodMood =Chain(monthlyQlty,sunnyToday,(quality: String, sunny: Boolean) =>
           if(sunny){
             if (quality == "good") Flip(0.9)
             else if(quality == "average") Flip(0.7)
             else Flip(0.4)
           }else{
             if (quality == "good") Flip(0.6)
             else if(quality == "average") Flip(0.3)
             else Flip(0.05)
           })

    println(VariableElimination.probability(goodMood,true))
  }
}
