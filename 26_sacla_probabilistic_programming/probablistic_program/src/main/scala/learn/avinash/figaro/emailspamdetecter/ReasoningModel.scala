package learn.avinash.figaro.emailspamdetecter

import java.util.Dictionary

import com.cra.figaro.language.Flip
import com.cra.figaro.library.atomic.discrete.Binomial
import com.cra.figaro.library.compound.If

class ReasoningModel(dictionary: Dictionary,
                     parameters: LearnedParameters) extends Model(dictionary){

  val isSpam = Flip(parameters.spamProbability)

  val hasWordElements = {
    for{word <- dictionary.featureWords } yield {
      val givenSpamProbability = parameters.wordGivenSpamProbabilities(word)
      val givenNormalProbability = parameters.wordGivenNormalProbabilities(word)
      val hasWordIfSpam = Flip(givenSpamProbability)
      val hasWordIfNormal = Flip(givenNormalProbability)
      val hasWord = If(isSpam, hasWordIfSpam,hasWordIfNormal)(word,hasWord)
    }
  }

  val hasManyUnusualIfSpam = Flip(parameters.hasManyUnusualWordsGivenSpamProbability)
  val hasManyUnusualIfNormal =  Flip(parameters.hasManyUnusualWordsGivenNormalProbability)
  val hasManyUnusualWords = If(isSpam,hasManyUnusualIfSpam, hasManyUnusualIfNormal)

  val numUnusualIfHasMany = Binomial(Model.binomialNumTrials,parameters.unusualWordGivenManyProbability )
  val numUnusualIfHasFew = Binomial(Model.binomialNumTrials,parameters.unusualWordGivenFewProbability )
  val numUnusyalWords = If(hasManyUnusualWords, numUnusualIfHasMany, numUnusualIfHasFew)

}
