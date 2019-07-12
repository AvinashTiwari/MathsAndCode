package learn.avinash.figaro.quicktutorial

import com.cra.figaro.algorithm.factored.VariableElimination
import com.cra.figaro.language.{Apply, Chain, Flip}
import com.cra.figaro.library.atomic.discrete.Binomial

object SimpleChaining {
  def main(args: Array[String]): Unit = {
    val numSunnyDaysInWeek = Binomial(30,0.2)

    val  teamWithInMonth = Binomial(5,0.4)
    val monthlyQlty = Apply(numSunnyDaysInWeek,teamWithInMonth, (days: Int, wins:Int) =>{
      val x = days * wins
      if( x > 20) "good"; else if(x >10) "average"; else "poor"
    } )

    val goodmood = Chain(monthlyQlty,(s:String) =>
       if(s == "good") Flip(0.9)
       else if(s == "average")  Flip(0.6)
       else Flip(0.1))

    println(VariableElimination.probability(goodmood, true))
  }
}
